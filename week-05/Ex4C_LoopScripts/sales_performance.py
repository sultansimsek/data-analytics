sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# 5. BONUS: Toplam satışları takip etmek için değişken
total_all_sales = 0

# 3. Döngü içinde tuple paketini doğrudan açma (name, region, sales)
for name, region, sales in sales_data:
    # Toplama ekleme yap
    total_all_sales += sales
    
    # Bilgileri yazdır (:,.2f binlik ayırıcı ve 2 basamaklı kuruş sağlar)
    print(f"{name} ({region}): ${sales:,.2f}")
    
    # 4. Koşul: 5000'den büyükse top performer yazdır
    if sales > 5000:
        print(" ^ Top performer!")


print("-" * 30)
print(f"Overall total sales: ${total_all_sales:,.2f}")