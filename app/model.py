class Users :
    buckets = []

    ##Add buckets.
    def add_item(self, name, time):
        ## Check if the name and time have been provided.
        if name and time:
            ## Create a dictionary to hold the new item.
            id = 1
            if len(self.buckets):
                id = len(self.buckets)

            dict = {'id': id, 'name': name, 'time': time}
            self.buckets.append(dict)
            return True

        return False

    ## Edit bucket
    def edit_bucket():
        pass

    ## Delete bucket
    def delete_bucket():
        pass

    ## List buckets.
    def list_items(self):
        return self.buckets   


class Bucket:
    bucketlist_items = []

    ##Add buckets.
    def add_item(self, name, time):
        ## Check if the name and time have been provided.
        if name and time:
            ## Create a dictionary to hold the new item.
            id = 1
            if len(self.bucketlist_items):
                id = len(self.bucketlist_items)

            dict = {'id': id, 'name': name, 'time': time}
            self.bucketlist_items.append(dict)
            return True

        return False

    ## Edit bucket
    def edit_item(self, id, name):
        ## The id cannnot be empty
        if id and name:
            for item in self.bucketlist_items:
                if item['id'] == id:
                    item['name'] = name
                    return True
                    
        return False

    ## Delete bucket
    def delete_item(self):
        pass

    ## List buckets.
    def list_items(self):
        pass             

class BucketItem:        
    bucketItems = []