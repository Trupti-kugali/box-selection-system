def product_fits_box(product, box):
    product_dimensions = sorted([
        product.length,
        product.width,
        product.height
    ])

    box_dimensions = sorted([
        box.length,
        box.width,
        box.height
    ])

    dimensions_fit = all(
        product_dimension <= box_dimension
        for product_dimension, box_dimension
        in zip(product_dimensions, box_dimensions)
    )

    weight_fits = product.weight <= box.max_weight

    return dimensions_fit and weight_fits


def recommend_box(product, boxes):
    suitable_boxes = []

    product_volume = (
        product.length *
        product.width *
        product.height
    )

    for box in boxes:

        if product_fits_box(product, box):

            box_volume = (
                box.length *
                box.width *
                box.height
            )

            unused_volume = box_volume - product_volume

            suitable_boxes.append(
                (unused_volume, box.cost, box)
            )

    if not suitable_boxes:
        return None

    suitable_boxes.sort(
        key=lambda item: (item[0], item[1])
    )

    return suitable_boxes[0][2]