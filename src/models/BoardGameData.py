from dataclasses import dataclass, fields, is_dataclass, asdict
import xml.etree.ElementTree as xe

# class CsvSerialized:
#     @classmethod
#     def get_csv_definition(cls) -> str:
#         return ','.join([field.type.get_csv_definition() if is_dataclass(field.type) else field.name for field in fields(cls)])
    
#     def to_csv(self) -> str:
#         # see shallow copy: https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict
#         data_fields = dict((field.name, getattr(self, field.name)) for field in fields(self)).items()
#         return ','.join(v.to_csv() if is_dataclass(v) else str(v) for k, v in data_fields)
    

@dataclass
class BoardGameInfo:
    id: int
    name: str
    numweights: int
    averageweight: float
    playingtime: int
    minage: int
    
    @classmethod
    def from_item(cls, item: xe):
        id = item.attrib['id']
        name = item.find('./name[@type=\'primary\']').attrib['value']
        ratings = item.find('./statistics/ratings')
        return cls(id, 
                   name, 
                   int(ratings.find('./numweights').attrib['value']), 
                   float(ratings.find('./averageweight').attrib['value']),
                   int(item.find('./playingtime').attrib['value']),
                   int(item.find('./minage').attrib['value'])
                  )
    
@dataclass
class BoardGame:
    info: BoardGameInfo
    rulebook: str
    
if __name__ == '__main__':
    b = BoardGame(BoardGameInfo(id='10', name='Elfenland', numweights=703, averageweight=2.1579, playingtime=60, minage=10), 'test')
    # print(b.get_csv_definition())
    # print(b.to_csv())