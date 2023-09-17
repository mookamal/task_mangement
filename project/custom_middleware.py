from pages.models import Info


class CustomMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        info = Info.objects.first()
        request.info = info
        path_board = "/b/"
        current_path = str(request.path)
        request.path_board = current_path.startswith(path_board)
        response = self.get_response(request)
        return response
