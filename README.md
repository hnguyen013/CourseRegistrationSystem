# Course Registration System

## 1. Giới thiệu

Course Registration System là ứng dụng quản lý đăng ký học phần được xây dựng bằng Python. Ứng dụng sử dụng giao diện đồ họa GUI Tkinter và cơ sở dữ liệu SQLite để quản lý sinh viên, giảng viên, học phần, đăng ký học phần và báo cáo thống kê.

---

## 2. Công nghệ sử dụng

* Python
* Tkinter
* ttk.Treeview
* SQLite
* CSV
* Git/GitHub

---

## 3. Chức năng chính

### Dashboard

* Hiển thị giao diện chính của hệ thống.
* Có sidebar để chuyển sang các trang:

  * Student
  * Lecturer
  * Course
  * Registration
  * Reports
* Có các thẻ chức năng để mở nhanh từng module.

### Student Management

* Thêm sinh viên.
* Cập nhật thông tin sinh viên.
* Xóa sinh viên.
* Tìm kiếm sinh viên theo mã, tên hoặc ngành học.
* Hiển thị danh sách sinh viên bằng bảng Treeview.

### Lecturer Management

* Thêm giảng viên.
* Cập nhật thông tin giảng viên.
* Xóa giảng viên.
* Hiển thị danh sách giảng viên.

### Course Management

* Thêm học phần.
* Cập nhật học phần.
* Xóa học phần.
* Hiển thị danh sách học phần.
* Phân loại học phần thành:

  * Compulsory Course
  * Elective Course

### Registration Management

* Đăng ký học phần cho sinh viên.
* Kiểm tra sinh viên có tồn tại hay không.
* Kiểm tra học phần có tồn tại hay không.
* Kiểm tra trùng đăng ký.
* Hiển thị danh sách đăng ký học phần.
* Tính tổng học phí của sinh viên.

### Reports

* Thống kê học phí theo từng sinh viên.
* Thống kê số lượng sinh viên đăng ký theo từng học phần.
* Xuất báo cáo ra file CSV trong thư mục `exports`.

---

## 4. Cấu trúc thư mục

```text
CourseRegistrationSystem/
│
├── main.py
│
├── database/
│   └── course_registration.db
│
├── exports/
│   └── report.csv
│
├── models/
│   ├── person.py
│   ├── student.py
│   ├── lecturer.py
│   ├── course.py
│   ├── compulsory_course.py
│   └── elective_course.py
│
├── services/
│   ├── database_service.py
│   ├── student_service.py
│   ├── lecturer_service.py
│   ├── course_service.py
│   └── registration_service.py
│
└── views/
    ├── base_view.py
    ├── dashboard_view.py
    ├── student_view.py
    ├── lecturer_view.py
    ├── course_view.py
    ├── registration_view.py
    ├── report_view.py
    └── style.py
```

---

## 5. Kiến trúc hệ thống

Dự án được chia theo mô hình phân tầng:

### models

Chứa các lớp đối tượng của hệ thống:

* Person
* Student
* Lecturer
* Course
* CompulsoryCourse
* ElectiveCourse

### services

Chứa phần xử lý dữ liệu và nghiệp vụ:

* Kết nối SQLite.
* Thêm, sửa, xóa, lấy dữ liệu.
* Xử lý đăng ký học phần.
* Tính tổng học phí.

### views

Chứa giao diện người dùng:

* Dashboard
* Student Management
* Lecturer Management
* Course Management
* Registration Management
* Reports

---

## 6. Cơ sở dữ liệu

Ứng dụng sử dụng SQLite với file:

```text
database/course_registration.db
```

Các bảng chính:

### students

Lưu thông tin sinh viên:

* student_id
* name
* email
* major

### lecturers

Lưu thông tin giảng viên:

* lecturer_id
* name
* email
* department

### courses

Lưu thông tin học phần:

* course_id
* course_name
* credits
* tuition_fee
* course_type

### registrations

Lưu thông tin đăng ký học phần:

* registration_id
* student_id
* course_id
* registration_date

---

## 7. Áp dụng lập trình hướng đối tượng

### Inheritance (Kế thừa)

Dự án sử dụng tính kế thừa để tái sử dụng mã nguồn và xây dựng mối quan hệ giữa các lớp.

* Lớp `Person` là lớp cha của:

  * `Student`
  * `Lecturer`

* Lớp `Course` là lớp cha của:

  * `CompulsoryCourse`
  * `ElectiveCourse`

### Encapsulation (Đóng gói)

Dự án áp dụng tính đóng gói thông qua việc sử dụng các thuộc tính private (`__attribute`) và các phương thức `@property`, setter để kiểm soát việc truy cập dữ liệu.

Các lớp áp dụng bao gồm:

* `Person`
* `Student`
* `Lecturer`
* `Course`

### Polymorphism (Đa hình)

Dự án áp dụng tính đa hình thông qua phương thức `get_course_type()`.

Lớp `Course` khai báo phương thức trừu tượng `get_course_type()`, sau đó các lớp con:

* `CompulsoryCourse`
* `ElectiveCourse`

ghi đè (override) phương thức này để trả về loại môn học tương ứng.

### Abstraction (Trừu tượng)

Dự án áp dụng tính trừu tượng thông qua lớp trừu tượng `Course` kế thừa từ `ABC`.

Phương thức `get_course_type()` được khai báo bằng `@abstractmethod`, buộc các lớp con phải triển khai theo cách riêng của mình.

---
## 8. Tự đánh giá theo thang điểm

Dựa trên tiêu chí chấm điểm của đề bài, chương trình được tự đánh giá như sau:

| STT | Tiêu chí                   | Điểm tối đa | Tự chấm | Giải thích                                                                                                                                                                          |
| --- | -------------------------- | ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Encapsulation              | 0.5         | 0.5     | Sử dụng private attribute (`__attribute`) và các phương thức `@property`, setter trong các lớp `Person`, `Student`, `Lecturer` và `Course` để bảo vệ dữ liệu và kiểm soát truy cập. |
| 2   | Inheritance                | 0.5         | 0.5     | `Student`, `Lecturer` kế thừa từ `Person`; `CompulsoryCourse`, `ElectiveCourse` kế thừa từ `Course`.                                                                                |
| 3   | Polymorphism & Abstraction | 1.0         | 1.0     | Sử dụng lớp trừu tượng `Course` (ABC) và phương thức `get_course_type()` được ghi đè trong các lớp con.                                                                             |
| 4   | Layered Architecture       | 1.0         | 1.0     | Dự án được chia thành các tầng riêng biệt gồm `models`, `services` và `views`, giúp dễ bảo trì và mở rộng.                                                                          |
| 5   | Clean Code (SRP)           | 0.5         | 0.5     | Các lớp được phân chia theo đúng trách nhiệm, tên lớp và phương thức rõ ràng, dễ hiểu.                                                                                              |
| 6   | Exception Handling         | 0.5         | 0.5     | Sử dụng `try-except` để xử lý lỗi nhập liệu và các thao tác với dữ liệu.                                                                                                            |
| 7   | CRUD Operations            | 1.0         | 1.0     | Hỗ trợ đầy đủ chức năng thêm, xem, sửa và xóa cho sinh viên, giảng viên, học phần và đăng ký học phần.                                                                              |
| 8   | Search & Sort              | 1.0         | 0.8     | Có chức năng tìm kiếm dữ liệu. Chức năng sắp xếp được triển khai ở mức cơ bản.                                                                                                      |
| 9   | Permanent Storage          | 1.0         | 1.0     | Dữ liệu được lưu trữ bằng SQLite và được giữ lại sau khi đóng chương trình.                                                                                                         |
| 10  | Complex Transaction Logic  | 1.0         | 1.0     | Chức năng đăng ký học phần kiểm tra dữ liệu hợp lệ, tránh đăng ký trùng và tính toán học phí tương ứng.                                                                             |
| 11  | Statistics & Export        | 1.0         | 1.0     | Có chức năng thống kê và xuất dữ liệu báo cáo ra file CSV.                                                                                                                          |
| 12  | Advanced Technology        | 0.5         | 0.5     | Sử dụng giao diện GUI Tkinter kết hợp cơ sở dữ liệu SQLite.                                                                                                                         |
| 13  | Git & GitHub Management    | 0.5         | 0.5     | Dự án được quản lý bằng Git và lưu trữ trên GitHub với lịch sử commit rõ ràng.                                                                                                      |

|  | **TỔNG CỘNG** | **10.0** | **9.8** |  |


### Nhận xét

Hệ thống đã hoàn thành hầu hết các yêu cầu của đề bài, bao gồm kiến trúc phân tầng, giao diện đồ họa, quản lý dữ liệu bằng SQLite, các chức năng CRUD, báo cáo thống kê và áp dụng các nguyên tắc lập trình hướng đối tượng. Một số nội dung như Encapsulation và Search & Sort có thể được mở rộng thêm để hoàn thiện hơn trong tương lai.

---

## 9. Kết quả đạt được

* Xây dựng được ứng dụng quản lý đăng ký học phần bằng Python.
* Có giao diện GUI bằng Tkinter.
* Có cơ sở dữ liệu SQLite.
* Có các chức năng quản lý sinh viên, giảng viên, học phần và đăng ký học phần.
* Có báo cáo thống kê và xuất file CSV.
* Có cấu trúc phân tầng rõ ràng.

---


## 10. Thành viên thực hiện

Họ và tên: Trần Hạnh Nguyên

Lớp: Tin 2E

Môn học: Programming Methods

Giảng viên hướng dẫn: ThS. Trần Văn Long
