import { clicks, route } from '@slidev/client/logic/nav'
import { injectionSlidevContext } from '@slidev/client/constants'
import { useContext } from '@slidev/client/composables/useContext'
import { reactive } from 'vue'

export default {
    install: (app, options) => {
        // from https://github.com/slidevjs/slidev/blob/main/packages/client/modules/context.ts

        const context = reactive(useContext(route, clicks))
        context.clicks_in_range = (start, end) =>
            context.nav.clicks >= start && context.nav.clicks <= end;
        app.provide(injectionSlidevContext, context)
    }
}