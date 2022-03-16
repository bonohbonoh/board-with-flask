from flask import request, session
from flask_restx import Resource

from apps.src.dto.request.Comment_request_dto import comment_request_dto
from apps.src.sevice.Comment_service import comment_service

comment_api = comment_request_dto.api


@comment_api.route('/')
class unnecessary_comment_id_api(Resource):
    registration_request = comment_request_dto.registration_dto

    @comment_api.expect(registration_request)
    def post(self):
        """댓글 등록"""
        return comment_service.registration_comment_service(request.json)


@comment_api.route('/<int:comment_id>')
class need_comment_id_api(Resource):

    @comment_api.expect(comment_request_dto.update_dto)
    def patch(self, comment_id):
        """댓글 수정"""
        return comment_service.update_comment_service(request.json, comment_id)

    @comment_api.expect(comment_request_dto.delete_dto)
    def delete(self, comment_id):
        """댓글 삭제"""
        return comment_service.delete_comment_service(request.json, comment_id)
