width = int(input('กว้าง'))
width = int(input('ยาว'))

def area (width, hight):
    reg = width * hight
    tri = (1/2 ) * width * hight
    print(f'reg = {reg} and tri = {tri}')
    return (reg,tri)

area_reg, area_tri = area(width, hight)
print("พื้นที่สี่เหลี่ยม: {area_reg}")
print(f"พื้นที่สามเหลี่ยม: {area_tri}")