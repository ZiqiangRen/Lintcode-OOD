import collections
class FriendshipService:
    
    def __init__(self):
        # do intialization if necessary
        self.followers = collections.defaultdict(set)
        self.followings = collections.defaultdict(set)
        

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        # write your code here
        return sorted(list(self.followers[user_id]))

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        # write your code here
        return sorted(list(self.followings[user_id]))
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        # write your code here
        self.followers[to_user_id].add(from_user_id)
        self.followings[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        # write your code here
        try:
            self.followers[to_user_id].remove(from_user_id)
            self.followings[from_user_id].remove(to_user_id)
        except:
            return
