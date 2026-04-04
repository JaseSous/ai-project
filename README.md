<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=header" width="100%"/>
<div align="center">
  <h1>Học phần: Cơ sở Trí tuệ Nhân tạo (AI)</h1>
  <p><b>Giảng viên hướng dẫn: TS. Đỗ Như Tài</b></p>
  
  <img src="https://github.com/user-attachments/assets/ca2e9e30-4131-4b9b-af1d-7ad6dcd8f148" width="120" height="120" alt="SGU Logo">
</div>

---

## Giới thiệu
Repository này chứa các bài tập thực hành và đồ án môn học **Cơ sở Trí tuệ Nhân tạo**. Dự án tập trung vào quy trình xây dựng mô hình học máy toàn diện: từ bước tiền xử lý dữ liệu, trích xuất đặc trưng cho đến đánh giá và tối ưu hóa các thuật toán phân lớp.

## Thông tin nhóm thực hiện

<table align="center">
  <tr>
    <th colspan="4">Thành viên nhóm</th>
  </tr>
  <tr>
    <td align="center"><b>Phạm Minh Khôi</b><br>[ 3124411135 ]</td>
    <td align="center"><b>Trương Thuận Phú</b><br>[ 3124411234 ]</td>
    <td align="center"><b>Nguyễn Hoàng Quân</b><br>[ 3124411250 ]</td>
    <td align="center"><b>Nguyễn Mạnh Thắng</b><br>[ 3124411283 ]</td>
  </tr>
</table>

---

## Cấu trúc dự án

### [TH06] Rút trích dữ liệu và Tiền xử lý
* **Mục tiêu:** Chuẩn bị dữ liệu thô cho bài toán phân lớp.
* **Kỹ thuật:** * Kiểm tra tính toàn vẹn (trùng lặp, giá trị thiếu).
    * Trực quan hóa qua *Box plot, Histogram, Heatmap*.
    * Xử lý biến danh mục (*One-hot encoding*) và chuẩn hóa (*Min-Max, Standard Scaling*).
* **Dataset:** `pima-indians-diabetes.csv`, `iris.csv`.

### [TH07] Bài toán Phân lớp (Classification)
* **Mục tiêu:** Thực nghiệm các thuật toán Scikit-learn phổ biến.
* **Quy trình:**
    * Chia tập dữ liệu: Hold-out (7/3) & K-fold Cross Validation.
    * Mô hình Baseline: `Logistic Regression`, `LDA`, `KNN`, `Decision Tree`, `Naive Bayes`, `SVM`.
    * Đánh giá: Accuracy, Precision, Recall, Confusion Matrix.

### [Do_an] Đồ án cuối khóa: Banknote Authentication
* **Đề tài:** Phân loại tiền thật/giả dựa trên đặc trưng ảnh (Wavelet Transform).
* **Mô hình triển khai:**
    * **Ensemble Learning:** AdaBoost, Gradient Boosting, Random Forest.
    * **Deep Learning:** Multi-layer Perceptron (MLP).
* **Sản phẩm:** Code thực nghiệm, Báo cáo chi tiết (`Report.docx`) và Slide thuyết trình.

---

## Thư viện sử dụng
Dự án sử dụng hệ sinh thái Python Data Science:
* **Xử lý dữ liệu:** `Pandas`, `NumPy`.
* **Trực quan hóa:** `Matplotlib`, `Seaborn`.
* **Học máy:** `Scikit-learn`.

## Hướng dẫn cài đặt

1. **Clone repository:**
   ```bash
   git clone [https://github.com/jasesous/ai-project.git](https://github.com/jasesous/ai-project.git)
   cd ai-project
   ```
2. Cài đặt môi trường:
  ```bash
  pip install pandas numpy matplotlib seaborn scikit-learn
  ```
3. Thực thi:
  Sử dụng Jupyter Notebook hoặc VS Code để mở các file .ipynb trong từng thư mục tương ứng.
<div align="center">
 
---

<i>Học kỳ II - Năm học 2025-2026</i>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=footer" width="100%"/>
