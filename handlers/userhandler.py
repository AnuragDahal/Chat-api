from models import schemas
from core.database import user_collection
from handlers.exception import ErrorHandler


class Validate:
    @staticmethod
    def verify_email(email: str):
        check_email = user_collection.find_one({"email": email})
        if check_email:
            return email
        raise ErrorHandler.NotFound("Email not found")


class UserManager:
    @staticmethod
    def create(request: schemas.User):
        """
        Insert a new student record.
        A unique `id` will be created and provided in the response.
        """
        duplicate_user = user_collection.find_one({"email": request.email})
        if not duplicate_user:
            new_user = user_collection.insert_one(
                request.model_dump(exclude=None))
            return {"id": str(new_user.inserted_id)}
        return ErrorHandler.ALreadyExists("User already exists")

    @staticmethod
    def read():
        """
        Retrieve all student records.
        """
        count = user_collection.count_documents({})
        if count > 0:
            users = user_collection.find()
            return users
        raise ErrorHandler.NotFound("No user found")

    @staticmethod
    def update(old_email: str, request: schemas.UpdateUserEmail):

        is_email = Validate.verify_email(old_email)
        if is_email:
            user = user_collection.find_one_and_update(
                {"email": old_email}, {"$set": request.model_dump(exclude=None)})
            updated_user = user_collection.find_one({"email": request.email})
            return updated_user
        raise ErrorHandler.NotFound("User not found")

    @staticmethod
    def delete(email: str):
        """
        Delete a student record.
        """
        user = user_collection.delete_one({"email": email})
        if user.deleted_count == 0:
            raise ErrorHandler.NotFound("User not found")
        return {"message": "User deleted successfully"}
