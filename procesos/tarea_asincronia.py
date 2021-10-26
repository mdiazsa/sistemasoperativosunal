import asyncio


async def main():
    print("Inicio función main")
    task1 = asyncio.create_task(imprimir("1"))
    task2 = asyncio.create_task(imprimir("2"))
    task3 = asyncio.create_task(imprimir("3"))
    
    await  task3
    
    print("Terminó la función main")


async def imprimir(texto):
    for i in range(3):
        print("Esto se ejecutó en el task #" + texto + "\n")
        await asyncio.sleep(0.5)



asyncio.run(main())
