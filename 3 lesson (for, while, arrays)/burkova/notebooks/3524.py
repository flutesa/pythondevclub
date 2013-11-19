ware_house = [int(input()), int(input()), int(input())]
box = [int(input()), int(input()), int(input())]
box_in_wh = [0, 0, 0, 0, 0, 0]

box_in_wh[0] = (ware_house[0] // box[0]) * (ware_house[1] // box[1]) * (ware_house[2] // box[2])
box_in_wh[1] = (ware_house[0] // box[0]) * (ware_house[1] // box[2]) * (ware_house[2] // box[1])
box_in_wh[2] = (ware_house[0] // box[1]) * (ware_house[1] // box[0]) * (ware_house[2] // box[2])
box_in_wh[3] = (ware_house[0] // box[1]) * (ware_house[1] // box[2]) * (ware_house[2] // box[0])
box_in_wh[4] = (ware_house[0] // box[2]) * (ware_house[1] // box[0]) * (ware_house[2] // box[1])
box_in_wh[5] = (ware_house[0] // box[2]) * (ware_house[1] // box[1]) * (ware_house[2] // box[0])

print(max(box_in_wh))
