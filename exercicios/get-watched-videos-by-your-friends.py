import collections

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        
        # Passo 1: Encontrar amigos no 'level' k usando BFS
        queue = collections.deque([id])
        visited = {id}
        
        current_level = 0
        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            current_level += 1
            
        #  todos os amigos do nível k
        
        video_counts = collections.Counter()
        for person_id in queue:
            for video in watchedVideos[person_id]:
                video_counts[video] += 1
        
        # sorted() usa uma tupla (frequência, nome) como chave de ordenação
        sorted_items = sorted(video_counts.items(), key=lambda item: (item[1], item[0]))
        
        #  apenas os nomes dos vídeos da lista ordenada
        return [video for video, count in sorted_items]