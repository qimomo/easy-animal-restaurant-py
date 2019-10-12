from restaurant_control import RestaurantControl

if __name__ == "__main__":
    choice = int(input('usb(0), wifi(1)'))
    restaurant = RestaurantControl()
    if choice == 1:
        ip_address = input('请输入手机 ip 地址:\n')
        port = input('请输入手机 port 端口,5555-5585')
        restaurant.connect(ip_address+':'+port)
    input('请将场景置于大厅后点任意键继续')
    
    while True:
        print('\n执行大厅操作\n')
        restaurant.go_to('hall')
        restaurant.order()
        restaurant.pick_site_money()
        restaurant.pick_hall_money()
        restaurant.click_propaganda(30)

        # restaurant.click_propaganda(20)
        print('\n执行厨房操作\n')
        restaurant.go_to('kitchen')
        restaurant.pick_kitchen_money()
        