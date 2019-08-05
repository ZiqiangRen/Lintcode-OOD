'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        self.unit = chunkSize
        self.service = BaseGFSClient()

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        res = ""
        index = 0
        tmp = self.service.readChunk(filename, index)
        while tmp:
            res += tmp
            index += len(tmp)
            tmp = self.service.readChunk(filename, index)
        return res if res else None

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # we need to make sure to overwrite all the existed content
        seen = self.read(filename)
        index = 0
        total = max(len(content), len(seen) if seen else 0) # look at here!
        while index < total:
            self.service.writeChunk(filename, index, content[index:index+self.unit])
            index += self.unit
