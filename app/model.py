from flask import session

class Users :
    buckets = []

    ##Add buckets.
    def add_bucket(self, name, time):
        ## Check if the name and time have been provided.
        if name and time:
            ## Create a dictionary to hold the new item.
            #id = 1
            #if len(self.buckets):
            id = len(self.buckets) + 1

            user_id = session['user_id']
            dict = {'id': id, 'name': name, 'time': time, 'user_id': user_id}
            self.buckets.append(dict)
            return {'success' : True}

        return {'success' : False}

    ## Edit bucket
    def edit_bucket(self, bucket_id, name, time):
        bucket_id = int(bucket_id)
        if name:
            for bucket in self.buckets:
                if bucket['id'] == bucket_id:
                    bucket['name'] = name
                    bucket['time'] = time

        return {'success' : True}

    ## Delete bucket
    def delete_bucket(self, bucket_id):
        bucket_id = int(bucket_id)
        if id:
            for bucket in self.buckets:
                if bucket['id'] == bucket_id:
                    self.buckets.remove(bucket)

        return {'success' : True}

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

    ##Add buckets items.
    def add_item(self, name, description, time, bucket_id):
        ## Check if the name and time have been provided.
        if name:
            ## Create a dictionary to hold the new item.
            id = len(self.bucketlist_items) + 1

            dict = {'id': id, 'name': name, 'description': description, 'time': time, 'bucket_id': bucket_id}
            self.bucketlist_items.append(dict)
            return {'success' : True}

        return {'success' : False}

    ## Edit bucket item
    def edit_item(self, bucket_id, name):
        ## The id cannnot be empty
        bucket_id = int(bucket_id)
        if id and name:
            for item in self.bucketlist_items:
                if item['id'] == id:
                    item['name'] = name
                    return True
                    
            return {'success' : True}

    ## Delete bucket item
    def delete_item(self, bucket_id):
        bucket_id = int(bucket_id)
        if id:
            for item in self.bucketlist_items:
                if item['id'] == bucket_id:
                    self.bucketlist_items.remove(item)

            return {'success' : True}

    ## List buckets.
    def bucket_items(self, bucket_id):
        items = [] # A list to hold the bucket items
        bucket_id = int(bucket_id)
        for bucket_item in self.bucketlist_items:
            if bucket_item['bucket_id'] == bucket_id:
                items.append(bucket_item)

        return items

class BucketItem:        
    bucketItems = []