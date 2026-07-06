interface HailstoneResponse {
    number: number;
    length: number;
}

type HailstoneArray = [number, number];

interface APIEndpoints {
    getHailstone: {
        request: {
            limit: number;
        };
        response: HailstoneArray;
    };
}

const HAILSTONE_CONTRACT: APIEndpoints = {
    getHailstone: {
        request: { limit: 0 },
        response: [0, 0]
    }
};

export type { HailstoneResponse, HailstoneArray, APIEndpoints };
