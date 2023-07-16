from aiohttp import web
import asyncpg


async def handle(request):
    # Establish a connection to PostgreSQL
    # conn = await asyncpg.connect(
    #     user='aiohttp', password='aiohttp', database='aiohttp', host='postgres'
    # )
    #
    # # Perform database operations
    # result = await conn.fetch('SELECT 1')
    #
    # # Close the database connection
    # await conn.close()
    #
    return web.Response(text="text3")

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8097)
