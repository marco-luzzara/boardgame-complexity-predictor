import { defineAppSetup } from '@slidev/types'
import navigation from '../plugins/navigation'

export default defineAppSetup(({ app, router }) => {
    // Vue App
    app.use(navigation)
})