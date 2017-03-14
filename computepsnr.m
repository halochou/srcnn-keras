gt = imread('butterfly_GT.bmp');
gt = rgb2ycbcr(gt);
gt = gt(:,:,1);
gt = gt(7:231,7:231,1);
%gt = gt(7:255,7:255,1);

ti = imread('sr.bmp');
%ti = ti(1:225,1:225,:);
if size(ti,3) > 1
    ti = rgb2ycbcr(ti);
    ti = ti(:,:,1);
end

psnr(ti, gt)