from rest_framework.test import APITestCase
from . import models

class TestAmenities(APITestCase):
    
    # 재활용을 위한 코드 
    NAME = "Amenity Test"
    DESC = "Amenity Des"
    
    URL = "/api/v1/rooms/amenities/"

    # 어메니티 객체를 생성하는 함수
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )
        
    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        data = response.json()
        print(data)

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test Dsc"

    # 어메니티 하나의 객체 생성
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2") 
        # pk가 2인 어메니티는 아직 존재하지 않음
        self.assertEqual(response.status_code, 404)
        #따라서 이 test는 404가 나옴
        
    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")

        # 어메니티 정보를 올바르게 가져온 경우
        self.assertEqual(response.status_code, 200)

        # data에 json 형태로 넣어준다
        data = response.json()

        # data의 name과 현재 name이 같은지 확인
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):
        put_amenity_name = "new amenity name"
        put_amenity_desc = "new amenity description"
        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={
                "name":put_amenity_name,
                "description":put_amenity_desc,
            }
        )
        
        data = response.json()
        # print(data)
        
        self.assertEqual(
            response.status_code, 200,
            "Not 200 status code"
        )
        
        self.assertEqual(
            data["name"],
            put_amenity_name,
        )
        
        self.assertEqual(
            data["description"],
            put_amenity_desc,
        )

    def test_delete_amenity(self):

        response = self.client.delete("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 204)