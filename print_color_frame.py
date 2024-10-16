from scaling import scale_image


def print_color_frame(frame, percent=30):
    resized_frame = scale_image(frame, percent)

    for row in resized_frame:
        for pixel in row:
            r, g, b = pixel
            print(f"\033[48;2;{b};{g};{r}m \033[0m", end="")
        print("")
