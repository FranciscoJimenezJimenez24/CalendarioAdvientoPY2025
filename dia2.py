def manufacture_gifts(giftsToProduce):
  listGifts = []
  for i in range (len(giftsToProduce)):
    if (giftsToProduce[i]["quantity"] > 0):
      for j in range(giftsToProduce[i]["quantity"]):
        listGifts.append(giftsToProduce[i]["toy"])
  return listGifts