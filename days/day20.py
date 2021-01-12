import math


def rotate_img(img, times):
    def rotate_once(img):
        L = len(img)
        new_img = ["" for i in range(L)]
        for i in range(L):
            for j in range(L):
                new_img[j] += img[i][j]
        return new_img

    for i in range(times):
        img = rotate_once(img)
    return img


def flip_img(img):
    L = len(img)
    for i in range(L // 2):
        tmp = img[i]
        img[i] = img[L - i - 1]
        img[L - i - 1] = tmp
    return img


class Tile:
    def get_edges(self):
        es = []
        L = len(self.img)
        es.append(self.img[0])
        es.append("".join([self.img[i][L - 1] for i in range(L)]))
        es.append(self.img[L - 1])
        es.append("".join([self.img[i][0] for i in range(L)]))

        return es

    def __init__(self, text):
        self.id = int(text[0][5:9])
        self.img = text[1:]
        self.edges = self.get_edges()
        self.neighbors = []
        self.neighbor_pos = []

    def all_edges(self):
        es = []
        es += self.edges
        es += [e[::-1] for e in self.edges]
        return es

    def num_neighbors(self):
        return len(self.neighbors)

    def add_if_neighbor(self, other):
        if other in self.neighbors:
            return None
        elif other is self:
            return None

        i = 0
        for e in other.all_edges():
            if e in self.all_edges():
                self.neighbors.append(other)
                self.neighbor_pos.append(i)
                return None
            i += 1

    def orient(self, img, pos):
        img = rotate_img(img, pos)

        for i in range(2):
            for j in range(4):
                if self.img[0] == img[0]:
                    return None
                self.img = rotate_img(self.img, 1)
            self.img = flip_img(self.img)

    def cropped(self):
        return [r[1:-1] for r in self.img[1:-1]


with open("inputs/input20.txt", "r") as f:
    lines = f.read()

tiles_raw = [l.splitlines() for l in lines.split("\n\n")]
tiles = [Tile(t) for t in tiles_raw if t]
for t1 in tiles:
    for t2 in tiles:
        t1.add_if_neighbor(t2)

product = 1

for t in tiles:
    if t.num_neighbors() == 2:
        product *= t.id

print(product)

# Part 2

grid_size = int(math.sqrt(len(tiles)))
print(grid_size)