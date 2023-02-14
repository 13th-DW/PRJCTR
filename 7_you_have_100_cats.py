def cats_in_hats():

    cats = [0 for i in range(100)]
    step = 0

    # run task
    for j in range(100):

        for hat in range(step, 100, step + 1):
            if cats[hat] == 0:
                cats[hat] = 1
            elif cats[hat] == 1:
                cats[hat] = 0

        step += 1

    cats_index = []

    # count what cats have hats)
    for cat_index in range(100):
        if cats[cat_index] == 1:
            cats_index.append(cat_index + 1)

    return cats_index
