# Ürün Takip Uygulaması

Bu Python uygulaması, bir dükkanın ürünlerini takip etmeye yönelik basit bir arayüz sağlar. Kullanıcılar, ürün ekleyebilir, güncelleyebilir, sorgulayabilir ve görüntüleyebilir.

## Kullanım

1. **Uygulamayı Çalıştırma:**
    - Uygulamayı başlatmak için `main.py` dosyasını çalıştırın.
    - Uygulama, bir ana pencere içinde ürün eklemek, güncellemek, sorgulamak ve görüntülemek için araçlar sağlar.

2. **Ürün Ekleme:**
    - "Ürünü Kaydet" butonuna tıklayarak yeni bir ürün ekleyebilirsiniz.
    - Ürün adı, alış fiyatı, satış fiyatı ve alış tarihi girmeniz gerekmektedir.

3. **Ürün Arama:**
    - "Ara" butonu ile bir ürünü ismine göre sorgulayabilirsiniz.
    - Boş bırakıldığında, tüm ürünleri görüntüler.

4. **Temizleme:**
    - "Temizle" butonları, ilgili alanları temizler.

## Dükkan Sınıfı

- `Dükkan` sınıfı, SQLite veritabanı üzerinde işlemleri gerçekleştirir.
- `Ürün` sınıfı, her bir ürünün temel özelliklerini tutar.

## Kütüphaneler

- PyQt5: Grafik arayüz oluşturmak için kullanılmıştır.
- SQLite3: Veritabanı işlemleri için kullanılmıştır.

## Geliştirme

1. Kodu bilgisayarınıza indirin:

    ```bash
    git clone https://github.com/kullanici/urun-takip-uygulamasi.git
    cd urun-takip-uygulamasi
    ```

2. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install PyQt5
    ```

3. Uygulamayı çalıştırın:

    ```bash
    python main.py
    ```

## Katkıda Bulunma

- Hataları bildirmek veya önerilerde bulunmak için [GitHub proje sayfası](https://github.com/kullanici/urun-takip-uygulamasi) üzerinden "Issues" bölümünü kullanabilirsiniz.
- Kodunuza katkıda bulunmak için "Pull Requests" gönderebilirsiniz.

## Lisans

Bu proje, [MIT lisansı](LICENSE) altında lisanslanmıştır.

---

# Product Tracking Application

This Python application provides a simple interface for tracking products in a store. Users can add, update, query, and view products.

## Usage

1. **Running the Application:**
    - To launch the application, run the `main.py` file.
    - The application provides tools within a main window to add, update, query, and view products.

2. **Adding a Product:**
    - You can add a new product by clicking the "Save Product" button.
    - You need to enter the product name, purchase price, selling price, and purchase date.

3. **Product Search:**
    - You can query a product by name using the "Search" button.
    - When left blank, it displays all products.

4. **Clearing:**
    - "Clear" buttons clear the respective fields.

## Shop Class

- The `Shop` class performs operations on the SQLite database.
- The `Product` class holds the basic attributes of each product.

## Libraries

- PyQt5: Used for creating the graphical interface.
- SQLite3: Used for database operations.

## Development

1. Clone the code to your computer:

    ```bash
    git clone https://github.com/user/product-tracking-application.git
    cd product-tracking-application
    ```

2. Install the required libraries:

    ```bash
    pip install PyQt5
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Contribution

- To report bugs or make suggestions, use the "Issues" section on the [GitHub project page](https://github.com/user/product-tracking-application).
- To contribute to the code, submit "Pull Requests."

## License

This project is licensed under the [MIT License](LICENSE).
