import webcolors


class GRB_Parser:

    def __init__(self):
        """
        pass in list of text colors like ['red', 'blue', 'green'] 
        and get back GRB hex version of those colors.
        """

    def convert(self, colors=[]):
        text_colors = colors
        int_colors = self.get_raw_colors(text_colors)
        colorgroups = [
            i.split('x')[1] for i in self.get_hexstring_colors(int_colors)
        ]
        return self.rgb_to_gbr(colorgroups)

    def get_raw_colors(self, colors):
        raw_colors = []
        for i in colors:
            raw_colors.append(
                int(webcolors.name_to_hex(i).replace('#', ''), 16))
        return raw_colors

    def get_hexstring_colors(self, colors):
        hexstr_colors = []
        for i in colors:
            hexstr_colors.append(hex(i))
        return hexstr_colors

    def rgb_to_gbr(self, colorgroups):
        grb_colors = []
        for i in colorgroups:
            if len(i) == 2:
                i = '0000' + i
            if len(i) == 4:
                i = '00' + i
            r, g, b = i[0:2], i[2:4], i[4:6]
            grb = int('0x' + g + r + b, 16)
            grb_colors.append(grb)
        return grb_colors

    def grb_gradient(self, color1, color2, density):
        c1 = self.convert([color1])
        c2 = self.convert([color2])
        chain = []
        cnt = 0
        for n in range(density):
            cnt += 1
            chain.append(div * cnt)
            if n % length == 0:
                if n < 0:
                    n = n * -1


if __name__ == '__main__':
    c = [
        'green', 'red', 'blue'
    ]
    print(GRB_Parser(colors=c).convert())
