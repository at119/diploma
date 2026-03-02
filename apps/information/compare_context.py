from apps.information.uni_compare import Compare



def get_compare(request):
    return {"compare":Compare(request)}
