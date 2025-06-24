describe('Helpers tests', function() {
  beforeEach(function() {
    allPayments = {};
  });

  it('should sum tipAmt correctly', function() {
    allPayments = {
      p1: {billAmt: '10', tipAmt: '2', tipPercent: 20},
      p2: {billAmt: '20', tipAmt: '4', tipPercent: 20}
    };
    expect(sumPaymentTotal('tipAmt')).toBe(6);
  });

  it('should sum billAmt correctly', function() {
    allPayments = {
      p1: {billAmt: '10', tipAmt: '2', tipPercent: 20},
      p2: {billAmt: '20', tipAmt: '4', tipPercent: 20}
    };
    expect(sumPaymentTotal('billAmt')).toBe(30);
  });

  it('should sum tipPercent correctly', function() {
    allPayments = {
      p1: {billAmt: '10', tipAmt: '2', tipPercent: 20},
      p2: {billAmt: '20', tipAmt: '4', tipPercent: 20}
    };
    expect(sumPaymentTotal('tipPercent')).toBe(40);
  });

  it('should calculate tip percent correctly', function() {
    expect(calculateTipPercent(100, 15)).toBe(15);
    expect(calculateTipPercent(50, 10)).toBe(20);
    expect(calculateTipPercent(10, 0)).toBe(0);
  });

  it('should append a td with correct value', function() {
    const tr = document.createElement('tr');
    appendTd(tr, 'test');
    expect(tr.children.length).toBe(1);
    expect(tr.children[0].innerText).toBe('test');
  });

  it('should append a delete button that removes the row on click', function() {
    const tr = document.createElement('tr');
    document.body.appendChild(tr); // Add to DOM for removal
    appendDeleteBtn(tr);
    expect(tr.children.length).toBe(1);
    expect(tr.children[0].innerText).toBe('X');
    // Simulate click
    tr.children[0].click();
    expect(document.body.contains(tr)).toBe(false);
  });
});
