#https://adventofcode.com/2021/day/20
import copy
def solve(file,its):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().strip().split("\n")
    enhancer,image = list(data[0]),data[2:]#index 2 to skip an empty line
    for idx,val in enumerate(image):
        image[idx] = list(val)
    edges = "." #what value the infinite expanse currently holds. Guaranteed to be same value
    for i in range(its):
        image = pad_image(image,edges)
        enhanced_image = copy.deepcopy(image)
        for idx, row in enumerate(image):
            for idx2, pixel in enumerate(row):
                enhanced_image[idx][idx2] = get_enhancement(edges,enhancer,image,idx,idx2)
        image = enhanced_image
        if edges == ".":
            edges = enhancer[0]
        else:
            edges = enhancer[511]

    for idx,val in enumerate(enhanced_image):
        enhanced_image[idx] = "".join(val)
    if edges == "#":
        #puzzle input is crafted in a way to never enter this branch, but
        #the puzzle description doesn't rule it out so this is a more complete solution.
        return "infinity"
    return sum(x.count("#") for x in enhanced_image)

def pad_image(image,edges):
    image.insert(0,[edges]*len(image[0]))
    image.append([edges]*len(image[0]))
    for row in image:
        row.insert(0,edges)
        row.append(edges)
    return image

def get_enhancement(edges,enhancer,image,idx,idx2):
    bin_string = ""
    for i in range(idx-1,idx+2):
        for j in range(idx2-1,idx2+2):
            try:
                bin_string += image[i][j]
            except IndexError:
                bin_string += edges
                continue
    bin_string = int(bin_string.replace(".","0").replace("#","1"),2)
    return enhancer[bin_string]
