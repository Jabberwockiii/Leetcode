class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(graph, k, res, path):
            path.append(k)
            if k == len(graph) - 1:
                res.append(path)
                return
            for i in graph[k]:
                path1 = copy.copy(path)
                dfs(graph, i, res, path)
                path = path1
        res = []
        dfs(graph, 0, res, [])
        return res
                