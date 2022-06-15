namespace screenMagic {
    /**
     * address LEDs linearly row first
     */
    //%blockId=screenmagicplotat
    export function lineIndex(index: number): void{
        index |= 0
        const x = Math.floor(index%5)
        const y = Math.floor(index/5)
        led.plot(x,y)
    }
}