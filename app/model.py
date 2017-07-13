from flask import session

class Users :
    buckets = []

    ##Add buckets.
    def add_bucket(self, name, time):
        ## Check if the name and time have been provided.
        if name and time:
            ## Create a dictionary to hold the new item.
            id = 1
            if len(self.buckets):
                id = len(self.buckets)

            user_id = session['user_id']
            dict = {'id': id, 'name': name, 'time': time, 'user_id': user_id}
            self.buckets.append(dict)
            return {'success' : True}

        return {'success' : False}

    ## Edit bucket
    def edit_bucket(self, id, name):
        pass

    ## Delete bucket
    def delete_bucket():
        pass

    ## List buckets.
    def list_items(self):
        user_id = session['user_id']
        bucket_listings = []
        for bucket in self.buckets:
            if bucket['user_id'] == user_id:
                bucket_listings.append(bucket)
                
        return bucket_listings   


class Bucket:
    bucketlist_items = []

    ##Add buckets.
    def add_item(self, name, description, time, bucket_id):
        ## Check if the name and time have been provided.
        if name:
            ## Create a dictionary to hold the new item.
            id = 1
            if len(self.bucketlist_items):
                id = len(self.bucketlist_items)

            dict = {'id': id, 'name': name, 'description': description, 'time': time, 'bucket_id': bucket_id}
            self.bucketlist_items.append(dict)
            return {'success' : True}

        return {'success' : False}

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
    def bucket_items(self, bucket_id):
        items = [] # A list to hold the bucket items
        for bucket_item in self.bucketlist_items:
            if bucket_item['bucket_id'] == bucket_id:
                items.append(bucket_item)

        return items

class BucketItem:        
    bucketItems = []