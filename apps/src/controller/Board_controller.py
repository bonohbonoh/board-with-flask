from flask import request
from flask_restx import Resource

from apps.src.dto.request.Board_request_dto import board_request_dto
from apps.src.dto.response.Board_response_dto import board_response_dto
from apps.src.sevice.Board_service import board_service

board_api = board_request_dto.api


@board_api.route('/')
class unnecessary_board_id_api(Resource):
    registration_request = board_request_dto.registration_dto

    @board_api.expect(registration_request)
    def post(self):
        """게시글 등록"""
        return board_service.registration_board_service(request.json)

    read_list_response = board_response_dto.read_list

    @board_api.expect(read_list_response)
    def get(self):
        """게시글 목록 조회"""
        return board_service.read_list_board_service(self)


@board_api.route('/<int:board_id>')
class need_board_id_api(Resource):

    @board_api.expect()
    def get(self, board_id):
        """게시글 상세 조회"""
        return board_service.read_detail_board_service(board_id)

    @board_api.expect(board_request_dto.update_dto)
    def patch(self, board_id):
        """게시글 수정"""
        return board_service.update_board_service(request.json, board_id)

    @board_api.expect()
    def delete(self, board_id):
        """게시글 삭제"""
        return board_service.delete_board_service(board_id)
