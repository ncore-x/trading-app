from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "1",
        "figi": "string",
        "instrument_type": "string",
        "date": "2023-11-21 06:50:49.523",
        "type": "Выплата купонов",
    }, follow_redirects=True)

    assert response.status_code == 200


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations", params={
        "operation_type": "Выплата купонов",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1
