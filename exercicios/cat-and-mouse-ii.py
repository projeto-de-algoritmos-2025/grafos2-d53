import collections

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        mouse_pos, cat_pos, food_pos = None, None, None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'M':
                    mouse_pos = (r, c)
                elif grid[r][c] == 'C':
                    cat_pos = (r, c)
                elif grid[r][c] == 'F':
                    food_pos = (r, c)

        # memoização p guardar os resultados dos estados
        memo = {}
        
        # limite de turnos p evitar loops
        max_turns = rows * cols * 2

        def solve(m_pos, c_pos, turn):
            state = (m_pos, c_pos, turn)
            if state in memo:
                return memo[state]

            # casos base / Condições de parada
            if turn >= max_turns or c_pos == food_pos or m_pos == c_pos:
                return False
            if m_pos == food_pos:
                return True

            # vez do rato
            if turn % 2 == 0:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for jump in range(mouseJump + 1):
                        mr, mc = m_pos[0] + dr * jump, m_pos[1] + dc * jump
                        
                        if not (0 <= mr < rows and 0 <= mc < cols and grid[mr][mc] != '#'):
                            break 
                        
                        if solve((mr, mc), c_pos, turn + 1):
                            memo[state] = True
                            return True
                
                memo[state] = False
                return False
            
            # vez do gato
            else:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    for jump in range(catJump + 1):
                        cr, cc = c_pos[0] + dr * jump, c_pos[1] + dc * jump

                        if not (0 <= cr < rows and 0 <= cc < cols and grid[cr][cc] != '#'):
                            break
                        
                        if not solve(m_pos, (cr, cc), turn + 1):
                            memo[state] = False
                            return False
                
                memo[state] = True
                return True

        return solve(mouse_pos, cat_pos, 0)