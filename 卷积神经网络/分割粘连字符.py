# 切割的位置
      im_position = CFS(im)

      maxL = max(im_position[0])
      minL = min(im_position[0])

      # 如果有粘连字符，如果一个字符的长度过长就认为是粘连字符，并从中间进行切割
      if(maxL > minL + minL * 0.7):
        maxL_index = im_position[0].index(maxL)
        minL_index = im_position[0].index(minL)
        # 设置字符的宽度
        im_position[0][maxL_index] = maxL // 2
        im_position[0].insert(maxL_index + 1, maxL // 2)
        # 设置字符X轴[起始，终点]位置
        im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
        im_position[1].insert(maxL_index + 1, [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
        # 设置字符的Y轴[起始，终点]位置
        im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])

      # 切割字符，要想切得好就得配置参数，通常 1 or 2 就可以
      cutting_img(im,im_position,img_name,1,1)
