

class Life:
    def __init__(self, grid):
        self.grid = grid

    def next_generation(self):
        next_gen = []
        for row in self.grid:
            next_gen_row = []
            for cell in row:
                # Find the number of neighbors
                count = row.count(True)
                if cell:
                    if count < 2:
                        next_gen_row.append(False)
                    elif 2 <= count <= 3:
                        next_gen_row.append(True)
                    else:
                        next_gen_row.append(False)
                else:
                    if count == 3:
                        next_gen_row.append(True)
                    else:
                        next_gen_row.append(False)
                        
                # Make the cell live / dead
                # Live cell:
                # < 2 => dead
                # 2 or 3 => alive
                # > 3 => dead
                # Dead cell:
                # == 3 => alive
                # anything else => dead
            next_gen.append(next_gen_row)
        return next_gen
