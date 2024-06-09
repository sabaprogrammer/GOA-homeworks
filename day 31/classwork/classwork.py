def diference_in_ages(ages):

    youngest = min(ages)

    oldest = max(ages)

    diference = oldest - youngest

    return youngest,oldest,diference

list=[12,432,52,523,2]

print(diference_in_ages(list))



