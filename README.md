# HỆ THỐNG QUẢN LÝ ĐĂNG KÝ HỌC PHẦN

(Course Registration Management System)

## 1. Giới thiệu

Hệ thống Quản lý Đăng ký Học phần là một ứng dụng được xây dựng bằng Python và thư viện Tkinter nhằm hỗ trợ quản lý sinh viên, giảng viên, học phần và quá trình đăng ký học phần trong môi trường đại học.

Dự án được phát triển nhằm đáp ứng yêu cầu của môn Programming Methods, áp dụng mô hình lập trình hướng đối tượng (OOP) và kiến trúc phân tầng (Layered Architecture).

---

## 2. Chức năng chính

### 2.1. Dashboard

* Hiển thị tổng quan hệ thống.
* Thống kê số lượng sinh viên.
* Thống kê số lượng giảng viên.
* Thống kê số lượng học phần.
* Thống kê số lượng đăng ký học phần.

### 2.2. Quản lý Sinh viên

* Thêm sinh viên mới.
* Cập nhật thông tin sinh viên.
* Xóa sinh viên.
* Tìm kiếm sinh viên theo mã hoặc tên.
* Hiển thị danh sách sinh viên.

### 2.3. Quản lý Giảng viên

* Thêm giảng viên mới.
* Chỉnh sửa thông tin giảng viên.
* Xóa giảng viên.
* Tìm kiếm giảng viên.
* Hiển thị danh sách giảng viên.

### 2.4. Quản lý Học phần

* Thêm học phần mới.
* Chỉnh sửa học phần.
* Xóa học phần.
* Tìm kiếm học phần.
* Hiển thị danh sách học phần.

### 2.5. Quản lý Đăng ký học phần

* Đăng ký học phần cho sinh viên.
* Hủy đăng ký học phần.
* Hiển thị danh sách đăng ký.
* Tính học phí dựa trên số tín chỉ.

### 2.6. Báo cáo và Thống kê

* Thống kê số lượng sinh viên đăng ký.
* Thống kê số lượng học phần.
* Báo cáo tổng số tín chỉ.
* Xuất báo cáo khi cần.

---

## 3. Áp dụng Lập trình Hướng đối tượng (OOP)

### Encapsulation (Đóng gói)

Các thuộc tính quan trọng được khai báo dưới dạng private và truy cập thông qua getter/setter.

### Inheritance (Kế thừa)

Course

* CompulsoryCourse (Môn bắt buộc)
* ElectiveCourse (Môn tự chọn)

Các lớp con kế thừa thuộc tính và phương thức từ lớp Course.

### Polymorphism (Đa hình)

Các lớp CompulsoryCourse và ElectiveCourse ghi đè các phương thức tính học phí hoặc hiển thị thông tin theo cách riêng.

### Abstraction (Trừu tượng)

Sử dụng lớp trừu tượng để định nghĩa các hành vi chung cho các đối tượng trong hệ thống.

---

## 4. Kiến trúc hệ thống

Dự án được xây dựng theo mô hình phân tầng gồm 3 lớp:

### models/

Chứa các lớp dữ liệu:

* Student
* Lecturer
* Course
* CompulsoryCourse
* ElectiveCourse
* Registration

### services/

Chứa các xử lý nghiệp vụ:

* StudentService
* LecturerService
* CourseService
* RegistrationService
* ReportService

### views/

Chứa giao diện người dùng:

* DashboardView
* StudentView
* LecturerView
* CourseView
* RegistrationView
* ReportView

---

## 5. Công nghệ sử dụng

* Python 3
* Tkinter
* ttk.Treeview
* JSON / SQLite
* Object-Oriented Programming (OOP)

---

## 6. Hướng dẫn cài đặt

### Bước 1: Clone dự án

```bash
git clone <link-github-cua-ban>
```

### Bước 2: Mở thư mục dự án

```bash
cd CourseRegistrationSystem
```

### Bước 3: Chạy chương trình

```bash
python main.py
```

---

## 7. Cấu trúc thư mục

```text
CourseRegistrationSystem/
│
├── models/
├── services/
├── views/
├── data/
│
├── main.py
└── README.md
```

---

## 8. Kết quả đạt được

* Xây dựng thành công hệ thống quản lý đăng ký học phần.
* Áp dụng đầy đủ 4 tính chất của OOP:

  * Encapsulation
  * Inheritance
  * Polymorphism
  * Abstraction
* Thực hiện đầy đủ các chức năng CRUD.
* Có chức năng tìm kiếm và thống kê.
* Xây dựng giao diện GUI bằng Tkinter.
* Tuân thủ kiến trúc phân tầng theo yêu cầu môn học.

---

## 9. Thành viên thực hiện

Họ và tên: ....................................

Lớp: ..........................................

Môn học: Programming Methods

Giảng viên hướng dẫn: ThS. Trần Văn Long

Trường Đại học Sư phạm - Đại học Huế
## 10. Đối chiếu với yêu cầu đồ án (Mapping to Assignment Requirements)

| Yêu cầu                              | Cách áp dụng trong hệ thống                                                                                                |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Encapsulation (0.5 điểm)             | Các thuộc tính quan trọng của Student, Lecturer, Course được đóng gói và truy cập thông qua các phương thức getter/setter. |
| Inheritance (0.5 điểm)               | Lớp Course là lớp cha, được kế thừa bởi CompulsoryCourse và ElectiveCourse.                                                |
| Polymorphism (1.0 điểm)              | Các lớp con ghi đè phương thức tính học phí hoặc hiển thị thông tin học phần theo từng loại môn học.                       |
| Abstraction (1.0 điểm)               | Sử dụng lớp trừu tượng làm khuôn mẫu cho các đối tượng trong hệ thống.                                                     |
| Layered Architecture (1.0 điểm)      | Dự án được chia thành 3 tầng: models, services và views.                                                                   |
| Clean Code (0.5 điểm)                | Tuân thủ quy tắc đặt tên, tách biệt chức năng theo từng lớp và module.                                                     |
| Exception Handling (0.5 điểm)        | Sử dụng try-except để xử lý lỗi nhập liệu và lỗi thao tác dữ liệu.                                                         |
| CRUD (1.0 điểm)                      | Hỗ trợ đầy đủ chức năng Thêm, Xem, Sửa và Xóa đối với sinh viên, giảng viên, học phần và đăng ký học phần.                 |
| Search & Sort (1.0 điểm)             | Hỗ trợ tìm kiếm theo mã hoặc tên và sắp xếp danh sách dữ liệu.                                                             |
| Permanent Storage (1.0 điểm)         | Dữ liệu được lưu trữ bằng SQLite và được tải lại khi khởi động chương trình.                                               |
| Complex Transaction Logic (1.0 điểm) | Chức năng đăng ký học phần tự động liên kết sinh viên với học phần và tính tổng học phí dựa trên số tín chỉ.               |
| Statistics & Reports (1.0 điểm)      | Hệ thống cung cấp các báo cáo thống kê số lượng sinh viên, học phần và đăng ký học phần.                                   |
| Advanced Technology (0.5 điểm)       | Xây dựng giao diện GUI bằng Tkinter và sử dụng SQLite Database để lưu trữ dữ liệu.                                         |
| Git & GitHub (0.5 điểm)              | Quản lý mã nguồn bằng Git, lưu trữ trên GitHub và cung cấp README hướng dẫn sử dụng.                                       |

### Tổng kết

Dự án đáp ứng đầy đủ các yêu cầu cơ bản và nâng cao của đề tài "Course Registration Management System", đồng thời áp dụng các nguyên tắc lập trình hướng đối tượng, kiến trúc phân tầng và giao diện đồ họa nhằm xây dựng một hệ thống quản lý học phần trực quan, dễ sử dụng và dễ mở rộng trong tương lai.
