import numpy as np
path="5/diem_2a.txt"
diem_2a = np.loadtxt(path,delimiter=',',dtype=np.int8)
diem_tb = []
for i in range(diem_2a.shape[1]):
    diem_tb.append(diem_2a[:,i].mean())
print("Điểm trung bình của từng học sinh trong lớp là:", diem_tb)
print("-------------------------------------------------")
print("điểm trung bình cao nhất là:", max(diem_tb))
print("của học sinh thứ:", diem_tb.index(max(diem_tb)))
print("bảng điểm đầy đủ của học sinh:", diem_2a[:,diem_tb.index(max(diem_tb))])
print("-------------------------------------------------")
print("điểm trung bình cao nhất là:", min(diem_tb))
print("của học sinh thứ:", diem_tb.index(min(diem_tb)))
print("bảng điểm đầy đủ của học sinh:", diem_2a[:,diem_tb.index(min(diem_tb))])
    
    
    