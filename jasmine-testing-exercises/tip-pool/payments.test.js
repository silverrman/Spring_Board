describe('Payments tests', function() {
  beforeEach(function() {
    billAmtInput.value = '';
    tipAmtInput.value = '';
    paymentTbody.innerHTML = '';
    allPayments = {};
    paymentId = 0;
  });

  it('should not create payment with empty inputs', function() {
    billAmtInput.value = '';
    tipAmtInput.value = '';
    expect(createCurPayment()).toBeUndefined();
  });

  it('should not create payment with negative bill', function() {
    billAmtInput.value = '-5';
    tipAmtInput.value = '2';
    expect(createCurPayment()).toBeUndefined();
  });

  it('should create payment object with valid inputs', function() {
    billAmtInput.value = '50';
    tipAmtInput.value = '10';
    const payment = createCurPayment();
    expect(payment).toEqual({billAmt: '50', tipAmt: '10', tipPercent: 20});
  });

  it('should append payment row to table', function() {
    billAmtInput.value = '20';
    tipAmtInput.value = '4';
    const payment = createCurPayment();
    paymentId = 1;
    appendPaymentTable(payment);
    expect(paymentTbody.children.length).toBe(1);
    expect(paymentTbody.children[0].children[0].innerText).toBe('$20');
    expect(paymentTbody.children[0].children[1].innerText).toBe('$4');
    expect(paymentTbody.children[0].children[2].innerText).toBe('20%');
  });

  it('should remove a payment row when delete button is clicked', function() {
    billAmtInput.value = '30';
    tipAmtInput.value = '6';
    const payment = createCurPayment();
    paymentId = 1;
    appendPaymentTable(payment);
    expect(paymentTbody.children.length).toBe(1);
    const row = paymentTbody.children[0];
    const deleteBtn = row.querySelector('td.deleteBtn');
    expect(deleteBtn).not.toBeNull();
    deleteBtn.click();
    expect(paymentTbody.children.length).toBe(0);
  });
});
