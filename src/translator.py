def translate_report_data(report_data):
    definition = {
        'Thu nhập lãi và các khoản thu nhập tương tự': 'interest_income_and_similar_income',
        'Chi phí lãi và các chi phí tương tự': 'interest_expense_and_similar_expenses',
        'Thu nhập lãi thuần': 'net_interest_income',
        'Thu nhập từ hoạt động dịch vụ': 'income_from_service_activities',
        'Chi phí hoạt động dịch vụ': 'service_activity_expenses',
        'Lãi thuần từ hoạt động dịch vụ': 'net_profit_from_service_activities',
        'Lãi/(lỗ) thuần từ hoạy động kinh doanh ngoại hối và vàng': 'net_profit_or_loss_from_foreign_exchange_and_gold_trading_activities',
        'Lãi/(lỗ) thuần từ mua bán chứng khoán kinh doanh': 'net_profit_or_loss_from_trading_securities_activities',
        'Lãi/(lỗ) thuần từ mua bán chứng khoán đầu tư': 'net_profit_or_loss_from_investment_securities_activities',
        'Thu nhập từ hoạt động khác': 'income_from_other_activities',
        'Chi phí hoạt động khác': 'other_operating_expenses',
        'Lãi/(lỗ) thuần từ hoạt động khác': 'net_profit_or_loss_from_other_activities',
        'Thu nhập từ góp vốn, mua cổ phần': 'income_from_contributions_share_purchases',
        'Tổng thu nhập hoạt động': 'total_operating_income',
        'Chi phí hoạt động': 'operating_expenses',
        'LN thuần từ hoạt động kinh doanh trước CF dự phòng rủi ro tín dụng': 'net_profit_from_business_operations_before_credit_risk_provisions',
        'Chi phí dự phòng rủi ro tín dụng': 'credit_risk_provisions_expenses',
        'Tổng lợi nhuận trước thuế': 'total_pre_tax_profit',
        'Chi phí thuế TNDN hiện hành': 'current_corporate_income_tax_expenses',
        'Chi phí thuế TNDN hoãn lại': 'deferred_corporate_income_tax_expenses',
        'Chi phí thuế thu nhập doanh nghiệp': 'income_tax_expenses',
        'Lợi nhuận sau thuế': 'profit_after_tax',
        'Lợi ích của cổ đông thiểu số': 'minority_interest',
        'Cổ đông của Công ty mẹ': 'shareholders_of_the_parent_company',
        'Lãi cơ bản trên cổ phiếu': 'basic_earnings_per_share',
        'Doanh số': 'revenue',
        'Các khoản giảm trừ': 'deductions',
        'Doanh số thuần': 'net_sales',
        'Giá vốn hàng bán': 'cost_of_goods_sold',
        'Lãi gộp': 'gross_profit',
        'Thu nhập tài chính': 'financial_income',
        'Chi phí tài chính': 'financial_expenses',
        'Trong đó: Chi phí lãi vay': 'interest_expense',
        'Lãi/(lỗ) từ công ty liên doanh': 'profit_or_loss_from_joint_ventures',
        'Chi phí bán hàng': 'selling_expenses',
        'Chi phí quản lý doanh  nghiệp': 'administrative_expenses',
        'Lãi/(lỗ) từ hoạt động kinh doanh': 'profit_or_loss_from_business_operations',
        'Thu nhập khác': 'other_income',
        'Chi phí khác': 'other_expenses',
        'Thu nhập khác, ròng': 'net_other_income',
        'Lãi/(lỗ) ròng trước thuế': 'net_profit_or_loss_before_tax',
        'Thuế thu nhập doanh nghiệp – hiện thời': 'current_corporate_income_tax',
        'Thuế thu nhập doanh nghiệp – hoãn lại': 'deferred_corporate_income_tax',
        'Chi phí thuế thu nhập doanh nghiệp': 'corporate_income_tax_expenses',
        'Lãi/(lỗ) thuần sau thuế': 'net_profit_or_loss_after_tax',
        'Lợi ích của cổ đông thiểu số': 'minority_interest',
        'Lợi nhuận của Cổ đông của Công ty mẹ': 'profit_attributable_to_shareholders_of_the_parent_company',
        'Lãi cơ bản trên cổ phiếu': 'basic_earnings_per_share',
        'Lãi trên cổ phiếu pha loãng': 'diluted_earnings_per_share',

        'Lưu chuyển tiền thuần từ các hoạt động sản xuất kinh doanh': 'net_cash_flow_from_operating_activities',
        'Lãi/lỗ trước những thay đổi vốn lưu động': 'profit_loss_before_changes_in_working_capital',
        'Lãi trước thuế': 'profit_before_tax',
        'Khấu hao TSCĐ': 'depreciation',
        'Chi phí dự phòng': 'provision_expenses',
        'Lãi/(lỗ) chênh lệch tỷ giá chưa thực hiện': 'unrealized_exchange_rate_gain_loss',
        'Lãi/(lỗ) từ thanh lý tài sản cố định': 'gain_loss_from_disposal_of_fixed_assets',
        'Lãi/(lỗ) từ hoạt động đầu tư': 'gain_loss_from_investment_activities',
        'Chi phí lãi vay': 'interest_expense',
        'Thu lãi và cổ tức': 'interest_and_dividend_received',
        'Các khoản điều chỉnh khác': 'other_adjustments',
        '(Tăng)/giảm các khoản phải thu': 'increase_decrease_in_accounts_receivable',
        '(Tăng)/giảm hàng tồn kho': 'increase_decrease_in_inventory',
        'Tăng/(giảm) các khoản phải trả': 'increase_decrease_in_accounts_payable',
        '( Tăng)/giảm chi phí trả trước': 'increase_decrease_in_prepaid_expenses',
        '(Tăng)/giảm chi phí trả trước': 'increase_decrease_in_prepaid_expenses',
        '(Tăng)/giảm chứng khoán kinh doanh': 'increase_decrease_in_trading_securities',
        'Chi phí lãi vay đã trả': 'interest_paid',
        'Thuế thu nhập doanh nghiệp đã trả': 'income_tax_paid',
        'Tiền thu khác từ các hoạt động kinh doanh': 'other_cash_receipts_from_operating_activities',
        'Tiền chi khác từ các hoạt động kinh doanh': 'other_cash_payments_from_operating_activities',
        'Lưu chuyển tiền tệ ròng từ hoạt động đầu tư': 'net_cash_flow_from_investing_activities',
        'Tiền mua tài sản cố định và các tài sản dài hạn khác': 'cash_paid_for_purchase_of_fixed_assets_and_other_long_term_assets',
        'Tiền thu được từ thanh lý tài sản cố định': 'cash_received_from_disposal_of_fixed_assets',
        'Tiền cho vay hoặc mua công cụ nợ': 'cash_loaned_or_advances_made',
        'Tiền thu từ cho vay hoặc thu từ phát hành công cụ nợ': 'cash_received_from_loans_or_advances',
        'Đầu tư vào các doanh nghiệp khác': 'investment_in_other_enterprises',
        'Tiền thu từ việc bán các khoản đầu tư vào các doanh nghiệp khác': 'cash_received_from_sale_of_investments_in_other_enterprises',
        'Cổ tức và tiền lãi nhận được': 'dividends_and_interest_received',
        'Lưu chuyển tiền tệ từ hoạt động tài chính': 'net_cash_flow_from_financing_activities',
        'Tiền thu từ phát hành cổ phiếu và vốn góp': 'cash_received_from_issuance_of_shares_and_contributions',
        'Chi trả cho việc mua lại, trả lại cổ phiếu': 'cash_paid_for_repurchase_or_return_of_shares',
        'Tiền thu được các khoản đi vay': 'cash_received_from_borrowings',
        'Tiển trả các khoản đi vay': 'cash_repayments_of_borrowings',
        'Tiền thanh toán vốn gốc đi thuê tài chính': 'cash_payments_of_principal_under_lease_financing',
        'Cổ tức đã trả': 'dividends_paid',
        'Tiền lãi đã nhận': 'interest_received',
        'Lưu chuyển tiền thuần trong kỳ': 'net_cash_flow_for_the_period',
        'Tiền và tương đương tiền đầu kỳ': 'cash_and_cash_equivalents_at_the_beginning_of_the_period',
        'Ảnh hưởng của chênh lệch tỷ giá': 'effect_of_exchange_rate_changes',
        'Tiền và tương đương tiền cuối kỳ': 'cash_and_cash_equivalents_at_the_end_of_the_period',

        "TỔNG TÀI SẢN": "Total Assets",
        "TÀI SẢN NGẮN HẠN": "Current Assets",
        "Tiền và tương đương tiền": "Cash and Cash Equivalents",
        "Tiền": "Cash",
        "Các khoản tương đương tiền": "Cash Equivalents",
        "Giá trị thuần đầu tư ngắn hạn": "Short-term Net Investment Value",
        "Đầu tư ngắn hạn": "Short-term Investments",
        "Dự phòng đầu tư ngắn hạn": "Provision for Short-term Investments",
        "Chứng khoán đầu tư giữ đến ngày đáo hạn": "Securities Held to Maturity",
        "Các khoản phải thu": "Accounts Receivable",
        "Phải thu khách hàng": "Accounts Receivable from Customers",
        "Trả trước người bán": "Prepayments to Suppliers",
        "Phải thu nội bộ": "Internal Receivables",
        "Phải thu về XDCB": "Receivables for Sale of Short-term Loans",
        "Phải thu về cho vay ngắn hạn": "Receivables for Short-term Loans",
        "Phải thu khác": "Other Receivables",
        "Dự phòng nợ khó đòi": "Provision for Difficult-to-Collect Debts",
        "Tài sản thiếu chờ xử lý": "Assets Held for Sale",
        "Hàng tồn kho, ròng": "Inventory, net",
        "Hàng tồn kho": "Inventory",
        "Dự phòng giảm giá HTK": "Provision for Inventory Impairment",
        "Tài sản lưu động khác": "Other Current Assets",
        "Trả trước ngắn hạn": "Short-term Prepayments",
        "Thuế VAT phải thu": "VAT Payable",
        "Phải thu thuế khác": "Other Taxes Payable",
        "Giao dịch mua bán lại trái phiếu chính phủ": "Purchase and Sale of Government Bonds",
        "Tài sản lưu động khác": "Other Current Assets",
        "TÀI SẢN DÀI HẠN": "Long-term Assets",
        "Phải thu dài hạn": "Long-term Receivables",
        "Phải thu khách hàng dài hạn": "Long-term Receivables from Customers",
        "Trả trước người bán dài hạn": "Long-term Prepayments to Suppliers",
        "Vốn kinh doanh ở các đơn vị trực thuộc": "Capital Invested in Subsidiaries",
        "Phải thu nội bộ dài hạn": "Long-term Internal Receivables",
        "Phải thu về cho vay dài hạn": "Long-term Receivables for Loans",
        "Phải thu dài hạn khác": "Other Long-term Receivables",
        "Dự phòng phải thu dài hạn": "Provision for Long-term Receivables",
        "Tài sản cố định": "Fixed Assets",
        "GTCL TSCĐ hữu hình": "Tangible Fixed Assets",
        "Nguyên giá TSCĐ hữu hình": "Original Cost of Tangible Fixed Assets",
        "Khấu hao lũy kế TSCĐ hữu hình": "Accumulated Depreciation of Tangible Fixed Assets",
        "GTCL Tài sản thuê tài chính": "Right-of-Use Assets",
        "Nguyên giá tài sản thuê tài chính": "Original Cost of Right-of-Use Assets",
        "Khấu hao lũy kế tài sản thuê tài chính": "Accumulated Depreciation of Right-of-Use Assets",
        "GTCL tài sản cố định vô hình": "Intangible Fixed Assets",
        "Nguyên giá TSCĐ vô hình": "Original Cost of Intangible Fixed Assets",
        "Khấu hao lũy kế TSCĐ vô hình": "Accumulated Depreciation of Intangible Fixed Assets",
        "Bất động sản đầu tư": "Investment Properties",
        "Nguyên giá tài sản đầu tư": "Original Cost of Investment Properties",
        "Khấu hao lũy kế tài sản đầu tư": "Accumulated Depreciation of Investment Properties",
        "Tài sản dở dang dài hạn": "Long-term Work in Progress",
        "Chi phí sản xuất, kinh doanh dở dang dài hạn": "Long-term Uncompleted Production and Business Expenses",
        "Đầu tư dài hạn": "Long-term Investments",
        "Đầu tư vào các công ty con": "Investments in Subsidiaries",
        "Đầu tư vào công ty liên doanh": "Investments in Joint Ventures",
        "Đầu tư dài hạn khác": "Other Long-term Investments",
        "Dự phòng giảm giá đầu tư dài hạn": "Provision for Long-term Investment Impairment",
        "Đầu tư nắm giữ đến ngày đáo hạn": "Investments Held to Maturity",
        "Tài sản dài hạn khác": "Other Long-term Assets",
        "Trả trước dài hạn": "Long-term Prepayments",
        "Thuế thu nhập hoãn lại phải thu": "Deferred Income Tax Payable",
        "Thiết bị, vật tư, phụ tùng thay thế dài hạn": "Long-term Equipment, Materials, Spare Parts",
        "Các tài sản dài hạn khác": "Other Long-term Assets",
        "NỢ PHẢI TRẢ": "Liabilities",
        "Nợ ngắn hạn": "Short-term Liabilities",
        "Phải trả người bán": "Accounts Payable",
        "Người mua trả tiền trước": "Customer Advances",
        "Thuế và các khoản phải trả Nhà nước": "Taxes and Other Payments to the State",
        "Phải trả người lao động": "Liabilities to Employees",
        "Chi phí phải trả": "Accrued Liabilities",
        "Phải trả nội bộ": "Internal Liabilities",
        "Phải trả về xây dựng cơ bản": "Liabilities for Basic Construction",
        "Doanh thu chưa thực hiện ngắn hạn": "Unearned Revenue",
        "Phải trả khác": "Other Liabilities",
        "Vay ngắn hạn": "Short-term Borrowings",
        "Dự phòng các khoản phải trả ngắn hạn": "Provision for Short-term Liabilities",
        "Quỹ khen thưởng, phúc lợi": "Reward and Welfare Fund",
        "Quỹ bình ổn giá": "Price Stabilization Fund",
        "Giao dịch mua bán lại trái phiếu chính phủ": "Purchase and Sale of Government Bonds",
        "Nợ dài hạn": "Long-term Liabilities",
        "Phải trả nhà cung cấp dài hạn": "Long-term Liabilities to Suppliers",
        "Người mua trả tiền trước dài hạn": "Customer Advances - Long-term",
        "Chi phí phải trả dài hạn": "Long-term Accrued Liabilities",
        "Phải trả nội bộ về vốn kinh doanh": "Internal Liabilities - Long-term",
        "Phải trả nội bộ dài hạn": "Internal Liabilities - Long-term",
        "Doanh thu chưa thực hiện": "Unearned Revenue - Long-term",
        "Phải trả dài hạn khác": "Other Long-term Liabilities",
        "Vay dài hạn": "Long-term Borrowings",
        "Trái phiếu chuyển đổi": "Convertible Bonds",
        "Thuế thu nhập hoãn lại phải trả": "Deferred Income Tax Liabilities",
        "Dự phòng các khoản công nợ dài hạn": "Provision for Long-term Liabilities",
        "Quỹ phát triển khoa học công nghệ": "Science and Technology Development Fund",
        "VỐN CHỦ SỞ HỮU": "Shareholders' Equity",
        "Vốn và các quỹ": "Capital and Reserves",
        "Vốn góp": "Capital Contributed",
        "Cổ phiếu phổ thông": "Common Stock",
        "Cổ phiếu ưu đãi": "Preferred Stock",
        "Thặng dư vốn cổ phần": "Additional Paid-in Capital",
        "Quyền chọn chuyển đổi trái phiếu": "Convertible Bond Conversion Rights",
        "Vốn khác": "Other Equity",
        "Cổ phiếu Quỹ": "Treasury Stock",
        "Chênh lệch đánh giá lại tài sản": "Revaluation Surplus",
        "Chênh lệch tỷ giá": "Foreign Currency Translation Adjustment",
        "Quỹ đầu tư và phát triển": "Investment and Development Fund",
        "Quỹ hỗ trợ sắp xếp doanh nghiệp": "Business Restructuring Support Fund",
        "Quỹ khác": "Other Funds",
        "Lãi chưa phân phối": "Undistributed Profit",
        "LNST chưa phân phối lũy kế đến cuối kỳ trước": "Accumulated Undistributed Profit at the End of the Previous Period",
        "LNST chưa phân phối kỳ này": "Undistributed Profit for the Current Period",
        "Lợi ích cổ đông không kiểm soát": "Non-controlling Interest",
        "Vốn Ngân sách nhà nước và quỹ khác": "State Budget Capital and Other Funds",
        "Vốn ngân sách nhà nước": "State Budget Capital",
        "Nguồn kinh phí đã hình thành TSCĐ": "Capital Sources Formed for Assets",
        "TỔNG CỘNG NGUỒN VỐN": "TOTAL SHAREHOLDERS' EQUITY"
    }
    for key, report in report_data.items():
        try:
            if 'CHỈ TIÊU' in report.columns:
                translated_column = report['CHỈ TIÊU'].map(definition)
                translated_column = translated_column.str.lower().str.replace(' ', '_')
                report['CHỈ TIÊU'] = translated_column
                report.set_index(["CHỈ TIÊU"], inplace=True)
                # print(f'{key} successfully translated')
            else:
                translated_column = report['Unnamed: 0'].map(definition)
                translated_column = translated_column.str.lower().str.replace(' ', '_')
                report['Unnamed: 0'] = translated_column
                report.set_index(['Unnamed: 0'], inplace=True)
                # print(f'{key} successfully translated')
        except KeyError as e:
            print(e)

