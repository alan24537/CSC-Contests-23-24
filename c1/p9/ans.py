# print((lambda tri, p: "yes" if (abs((tri[0]*tri[3] + tri[2]*tri[5] + tri[4]*tri[1]) - (tri[1]*tri[2] + tri[3]*tri[4] + tri[5]*tri[0]))/2.0) == (abs((p[0]*tri[3] + tri[2]*tri[5] + tri[4]*p[1]) - (p[1]*tri[2] + tri[3]*tri[4] + tri[5]*p[0]))/2.0) + (abs((tri[0]*p[1] + p[0]*tri[5] + tri[4]*tri[1]) - (tri[1]*p[0] + p[1]*tri[4] + tri[5]*tri[0]))/2.0) + (abs((tri[0]*tri[3] + tri[2]*p[1] + p[0]*tri[1]) - (tri[1]*tri[2] + tri[3]*p[0] + p[1]*tri[0]))/2.0) else "no")(list(map(int, input().split())), list(map(int, input().split()))))

def tri_area(A, B, C):
    return abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - (A[1]*B[0] + B[1]*C[0] + C[1]*A[0])) / 2.0

a1, a2, b1, b2, c1, c2 = map(int, input().split())
p1, p2 = map(int, input().split())

if tri_area((a1, a2), (b1, b2), (p1, p2)) + tri_area((b1, b2), (c1, c2), (p1, p2)) + tri_area((c1, c2), (a1, a2), (p1, p2)) == tri_area((a1, a2), (b1, b2), (c1, c2)):
    print("yes")
else:
    print("no")