async def health_check(request):
    message = "Server Running"

    return {
        "message": message,
    }
