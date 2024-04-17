class cart:
    def __init__(self,Imageurl,Price,Rating,Description,Delivery,Comments,Brandname):
        self.image = Imageurl
        self.price = Price
        self.rating = Rating
        self.description = Description
        self.delivery = Delivery
        self.comments = Comments
        self.brandname = Brandname

    def printalldetails(self):
            print("product inage is:",self.image)
            print("price",self.price)
            print("rating",self.rating)
            print("description",self.description)
            print("delivery",self.delivery)
            print("comments",self.comments)
            print("brandname",self.brandname)
    
    # def calculateGST(self):
    #     print("calculating gst")
    #     #logic

    # def printinvoice(self,extrapoints):
    #     print("printing invoice")
    #     #logic

    







    # obj123 = cart()
    # obj123.printinvoice(1200)
    # obj123.calculateGST()
    # obj201=cart()
    # obj201.calculateGST()


laptop=cart("laptop/fk",60000,5.0,"high storage high speed","5 days","good","lenovo")
laptop.printalldetails()

Smartwatch=cart("watch/amazon",8000,4.5,"more features","2 days","average","firebolt")
Smartwatch.printalldetails()

Mobile=cart("mobile/amazon",75000,10.00,"tere aukat ke bahar hai","shakal dekh le","best","abc")
Mobile.printalldetails()
