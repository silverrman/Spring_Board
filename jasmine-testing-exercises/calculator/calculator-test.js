
it('should calculate the monthly rate correctly', function () {
  const values = { amount: 10000, years: 5, rate: 5 };
  expect(calculateMonthlyPayment(values)).toBe('188.71');
});


it("should return a result with 2 decimal places", function() {
  const values = { amount: 12345, years: 3, rate: 4.5 };
  const result = calculateMonthlyPayment(values);
  expect(result).toMatch(/^\d+\.\d{2}$/);
});

it('should handle zero interest correctly', function() {
  const values = { amount: 12000, years: 4, rate: 0 };
  expect(calculateMonthlyPayment(values)).toBe('250.00');
});

it('should handle 1 year loan', function() {
  const values = { amount: 1200, years: 1, rate: 10 };
  expect(calculateMonthlyPayment(values)).toBe('105.49');
});

it('should handle very small principal', function() {
  const values = { amount: 1, years: 1, rate: 1 };
  expect(calculateMonthlyPayment(values)).toBe('0.08');
});

it('should handle very long term', function() {
  const values = { amount: 100000, years: 40, rate: 3 };
  expect(calculateMonthlyPayment(values)).toBe('357.08');
});

it('should round correctly for repeating decimals', function() {
  const values = { amount: 1000, years: 3, rate: 7 };
  expect(calculateMonthlyPayment(values)).toBe('30.88');
});
