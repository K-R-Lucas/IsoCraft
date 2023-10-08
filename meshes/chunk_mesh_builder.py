from settings import *

r = 1
c30 = (glm.cos(glm.radians(30)) + 0) * r
c150 = (glm.cos(glm.radians(150)) + 0) * r
c210 = (glm.cos(glm.radians(210)) + 0) * r
c330 = (glm.cos(glm.radians(330)) + 0) * r

s30 = (glm.sin(glm.radians(30)) + 0) * r
s150 = (glm.sin(glm.radians(150)) + 0) * r
s210 = (glm.sin(glm.radians(210)) + 0) * r
s330 = (glm.sin(glm.radians(330)) + 0) * r

def is_void(block_pos, chunk_blocks):
    x, y, z = block_pos

    if (x >= 0 and x < CHUNK_WIDTH) and (y >= 0 and y < CHUNK_HEIGHT) and (z >= 0 and z < CHUNK_DEPTH):
        if chunk_blocks[x + y*CHUNK_WIDTH + z*CHUNK_AREA] > 0:
            return False
    
    return True

def addVertexData(vertex_data, index, *vertices):
    for vertex in vertices:
        for i, attr in enumerate(vertex):
            vertex_data[index] = attr
            index += 1
    
    return index

def buildChunkMesh(chunk_blocks, format_size):
    vertex_data = np.empty(CHUNK_VOLUME * 18 * format_size, dtype="f")
    index = 0

    for z in range(CHUNK_DEPTH):
        for y in range(CHUNK_HEIGHT):
            for x in range(CHUNK_WIDTH):
                block_id = chunk_blocks[x + y*CHUNK_WIDTH + z*CHUNK_AREA]
                X = c30 * (x + z)
                Y = y + s30 * (x - z)
                Z = 0

                if block_id == 0:
                    continue

                # Top Face
                if is_void((x, y+1, z), chunk_blocks):
                    v0 = (X, Y, Z, block_id, 0)
                    v1 = (X + c30, Y + s30, Z, block_id, 0)
                    v2 = (X, Y + r, Z, block_id, 0)
                    v3 = (X + c150, Y + s150, Z, block_id, 0)

                    index = addVertexData(vertex_data, index, v0, v1, v2, v0, v2, v3)
                
                # Side Face
                if is_void((x-1, y, z), chunk_blocks):
                    v0 = (X, Y, Z, block_id, 1)
                    v1 = (X + c150, Y + s150, Z, block_id, 1)
                    v2 = (X + c210, Y + s210, Z, block_id, 1)
                    v3 = (X, Y - r, Z, block_id, 1)

                    index = addVertexData(vertex_data, index, v0, v1, v2, v0, v2, v3)
                
                # Front Face
                if is_void((x, y, z+1), chunk_blocks):
                    v0 = (X, Y, Z, block_id, 2)
                    v1 = (X, Y - r, Z, block_id, 2)
                    v2 = (X + c330, Y + s330, Z, block_id, 2)
                    v3 = (X + c30, Y + s30, Z, block_id, 2)

                    index = addVertexData(vertex_data, index, v0, v1, v2, v0, v2, v3)
    
    return vertex_data[:(index + 1)]