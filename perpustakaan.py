import logging
import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Define Pydantic model for Buku
class BukuCreate(BaseModel):
    judul: str
    penulis: str
    penerbit: Optional[str] = None
    tahun_terbit: Optional[int] = None
    konten: str
    iktsar: Optional[str] = None

class BukuUpdate(BaseModel):
    penerbit: Optional[str] = None
    tahun_terbit: Optional[int] = None
    iktsar: Optional[str] = None

class Buku(BaseModel):
    id: int
    judul: str
    penulis: str
    penerbit: Optional[str] = None
    tahun_terbit: Optional[int] = None
    konten: str
    iktsar: Optional[str] = None

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='',  # Replace with your MySQL password
        database='perpustakaan'  # Replace with your database name
    )

@app.on_event("startup")
async def startup_event():
    create_table()

@app.post("/buku/", response_model=dict)
async def create_buku(buku: BukuCreate):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                buku.judul,
                buku.penulis,
                buku.penerbit,
                buku.tahun_terbit,
                buku.konten,
                buku.iktsar
            )
            cursor.execute(query, values)
            connection.commit()
        logging.info(f"Buku '{buku.judul}' berhasil disimpan.")
        return {"status": "success", "message": f"Buku '{buku.judul}' berhasil disimpan."}
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/buku/{id_buku}", response_model=Buku)
async def read_buku(id_buku: int):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM buku WHERE id = %s"
            cursor.execute(query, (id_buku,))
            result = cursor.fetchone()
        if result:
            logging.info(f"Buku dengan ID {id_buku} ditemukan.")
            return Buku(
                id=result[0],
                judul=result[1],
                penulis=result[2],
                penerbit=result[3],
                tahun_terbit=result[4],
                konten=result[5],
                iktsar=result[6]
            )
        else:
            logging.warning(f"Buku dengan ID {id_buku} tidak ditemukan.")
            raise HTTPException(status_code=404, detail=f"Buku dengan ID {id_buku} tidak ditemukan.")
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.put("/buku/{id_buku}", response_model=dict)
async def update_buku(id_buku: int, buku: BukuUpdate):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            update_fields = []
            values = []
            if buku.penerbit is not None:
                update_fields.append("penerbit = %s")
                values.append(buku.penerbit)
            if buku.tahun_terbit is not None:
                update_fields.append("tahun_terbit = %s")
                values.append(buku.tahun_terbit)
            if buku.iktsar is not None:
                update_fields.append("iktisar = %s")
                values.append(buku.iktsar)
            if not update_fields:
                raise HTTPException(status_code=400, detail="No fields to update")
            
            query = f"UPDATE buku SET {', '.join(update_fields)} WHERE id = %s"
            values.append(id_buku)
            cursor.execute(query, values)
            connection.commit()
        logging.info(f"Buku dengan ID {id_buku} berhasil diperbarui.")
        return {"status": "success", "message": f"Buku dengan ID {id_buku} berhasil diperbarui."}
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.delete("/buku/{id_buku}", response_model=dict)
async def delete_buku(id_buku: int):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            query = "DELETE FROM buku WHERE id = %s"
            cursor.execute(query, (id_buku,))
            connection.commit()
        if cursor.rowcount:
            logging.info(f"Buku dengan ID {id_buku} berhasil dihapus.")
            return {"status": "success", "message": f"Buku dengan ID {id_buku} berhasil dihapus."}
        else:
            logging.warning(f"Buku dengan ID {id_buku} tidak ditemukan.")
            raise HTTPException(status_code=404, detail=f"Buku dengan ID {id_buku} tidak ditemukan.")
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/", response_model=List[Buku])
async def root():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM buku"
            cursor.execute(query)
            results = cursor.fetchall()
        books = [Buku(
            id=row[0],
            judul=row[1],
            penulis=row[2],
            penerbit=row[3],
            tahun_terbit=row[4],
            konten=row[5],
            iktsar=row[6]
        ) for row in results]
        logging.info("Menampilkan daftar buku.")
        return books
    except mysql.connector.Error as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

def create_table():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS buku (
                id INT AUTO_INCREMENT PRIMARY KEY,
                judul VARCHAR(255) NOT NULL,
                penulis VARCHAR(255) NOT NULL,
                penerbit VARCHAR(255),
                tahun_terbit INT,
                konten TEXT NOT NULL,
                iktisar TEXT
            )
            """
            cursor.execute(query)
            connection.commit()
        logging.info("Tabel buku berhasil dibuat.")
    except mysql.connector.Error as e:
        logging.error(f"Database error saat membuat tabel: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
