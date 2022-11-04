from typing import Type
import dataclasses
from dataclass_csv import DataclassReader

def extend_DataclassReader_with_nested_dataclass(dcr: Type[DataclassReader]) -> Type[DataclassReader]:
    def _extended_process_row(self, row):
        values = dict()

        for field in dataclasses.fields(self._cls):
            if not field.init:
                continue

            try:
                value = self._get_value(row, field)
            except ValueError as ex:
                raise CsvValueError(ex, line_number=self._reader.line_num) from None

            if not value and field.default is None:
                values[field.name] = None
                continue

            field_type = self.type_hints[field.name]

            # TODO: add strtobool  from dataclass_reader.py if necessary
            if field_type is bool:
                try:
                    transformed_value = (
                        value
                        if isinstance(value, bool)
                        else strtobool(str(value).strip()) == 1
                    )
                except ValueError as ex:
                    raise CsvValueError(ex, line_number=self._reader.line_num) from None
                else:
                    values[field.name] = transformed_value
                    continue
                    
            if dataclasses.is_dataclass(field_type):
                import ast
                fields = ast.literal_eval(value)
                values[field.name] = field_type(*fields)
                continue

            try:
                transformed_value = field_type(value)
            except ValueError as e:
                raise CsvValueError(
                    (
                        f"The field `{field.name}` is defined as {field.type} "
                        f"but received a value of type {type(value)}."
                    ),
                    line_number=self._reader.line_num,
                ) from e
            else:
                values[field.name] = transformed_value
        return self._cls(**values)
    dcr._process_row = _extended_process_row
    return dcr