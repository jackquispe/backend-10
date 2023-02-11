import prisma from '@prisma/client'

// asi se exporta de manera por defecto ( en el caso que tengamos un asola exportacion en nuestro archivo)
// solamnetre se puede tener una expportacion por defecto
export default new prisma.PrismaClient({
    log: ['query'],
})




