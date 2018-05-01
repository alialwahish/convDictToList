def dictToList(my_dict):
    li=[]
    for item in my_dict.items():
        li.append(item)  
    print li

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
dictToList(my_dict)


