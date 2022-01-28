import asyncio
import aiomysql.sa as aio_sa


async def main():
    # 创建一个异步引擎
    engine = await aio_sa.create_engine(host="xx.xxx.xx.xxx",
                                        port=3306,
                                        user="root",
                                        password="root",
                                        db="_hanser",
                                        connect_timeout=10)

    # 通过 engine.acquire() 获取一个连接
    async with engine.acquire() as conn:
        # 异步执行, 返回一个 <class 'aiomysql.sa.result.ResultProxy'> 对象
        result = await conn.execute("SELECT * FROM girl")
        # 通过 await result.fetchone() 可以获取满足条件的第一条记录, 一个 <class 'aiomysql.sa.result.RowProxy'> 对象
        data = await result.fetchone()

        # 可以将 <class 'aiomysql.sa.result.RowProxy'> 对象想象成一个字典
        print(data.keys())  # KeysView((1, '古明地觉', 16, '地灵殿'))
        print(list(data.keys()))  # ['id', 'name', 'age', 'place']