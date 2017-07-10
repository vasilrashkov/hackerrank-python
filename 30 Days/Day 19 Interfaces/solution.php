class Calculator implements AdvancedArithmetic
{
    public function divisorSum($n)
    {
        $sum = 0;
        $divisor = 1;
        while ($divisor <= $n) {
            if ($n % $divisor == 0) {
                $sum += $divisor;
            }

            $divisor++;
        }

        return $sum;
    }
}